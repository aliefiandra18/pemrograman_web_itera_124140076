/**
 * Deadline Radar - Personal Dashboard Mahasiswa
 * Praktikum PAW, Pertemuan 2 (JavaScript ES6+)
 */

// ---------- Konstanta (const) ----------
const WEATHER_URL = 'https://api.open-meteo.com/v1/forecast?latitude=-5.36&longitude=105.31&current_weather=true';
const QUOTE_URL = 'https://dummyjson.com/quotes/random';
const MS_PER_DAY = 86_400_000;

// ---------- Fungsi bantu (arrow functions) ----------
const escapeHtml = (text) => text.replace(/[&<>"']/g, (ch) => `&#${ch.charCodeAt(0)};`);

const formatDate = (iso) =>
  new Date(`${iso}T00:00:00`).toLocaleDateString('id-ID', { day: 'numeric', month: 'short', year: 'numeric' });

const describeWeather = (code) => {
  if (code === 0) return 'Cerah';
  if (code <= 3) return 'Berawan';
  if (code <= 48) return 'Berkabut';
  if (code <= 67) return 'Hujan';
  if (code <= 82) return 'Hujan deras';
  return 'Badai petir';
};

// ---------- Class 1: model data satu tugas ----------
class TaskItem {
  constructor({ id = `${Date.now().toString(36)}${Math.random().toString(36).slice(2, 6)}`,
    title, course = '', deadline = '', done = false }) {
    this.id = id;
    this.title = title;
    this.course = course;
    this.deadline = deadline;
    this.done = done;
  }

  // Selisih hari antara hari ini dan tenggat (null jika tanpa tenggat)
  get daysLeft() {
    if (!this.deadline) return null;
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    return Math.round((new Date(`${this.deadline}T00:00:00`) - today) / MS_PER_DAY);
  }

  // Menentukan warna garis kiri kartu: late, soon, ok, calm
  get urgency() {
    const days = this.daysLeft;
    if (this.done || days === null) return 'calm';
    if (days < 0) return 'late';
    return days <= 2 ? 'soon' : 'ok';
  }

  get statusLabel() {
    const days = this.daysLeft;
    if (this.done) return 'Selesai';
    if (days === null) return 'Tanpa tenggat';
    if (days < 0) return `Terlambat ${-days} hari`;
    if (days === 0) return 'Hari ini';
    return days === 1 ? 'Besok' : `${days} hari lagi`;
  }
}

// ---------- Class 2: state, localStorage, dan fetch ----------
class DashboardApp {
  static STORAGE_KEY = 'deadline-radar:tasks';

  constructor() {
    this.tasks = this.load();
    this.filter = 'all';
    this.editingId = null;
    this.dom = {
      form: document.querySelector('#task-form'),
      list: document.querySelector('#task-list'),
      filters: document.querySelector('#filters'),
      submit: document.querySelector('#submit-btn'),
      cancel: document.querySelector('#cancel-edit'),
      statsText: document.querySelector('#stats-text'),
      statsBar: document.querySelector('#stats-bar'),
      clock: document.querySelector('#clock'),
      date: document.querySelector('#date'),
      greeting: document.querySelector('#greeting'),
      weather: document.querySelector('#weather'),
      quote: document.querySelector('#quote'),
    };
    this.bindEvents();
    this.render();
    this.startClock();
    this.loadWeather();
    this.loadQuote();
  }

  // ----- localStorage -----
  load() {
    try {
      const raw = JSON.parse(localStorage.getItem(DashboardApp.STORAGE_KEY) ?? '[]');
      return raw.map((data) => new TaskItem(data));
    } catch {
      return [];
    }
  }

  commit() {
    localStorage.setItem(DashboardApp.STORAGE_KEY, JSON.stringify(this.tasks));
    this.render();
  }

  // ----- CRUD (spread operator: array state tidak diubah langsung) -----
  addTask({ title, course, deadline }) {
    this.tasks = [new TaskItem({ title, course, deadline }), ...this.tasks];
    this.commit();
  }

  updateTask(id, changes) {
    this.tasks = this.tasks.map((task) => (task.id === id ? new TaskItem({ ...task, ...changes }) : task));
    this.commit();
  }

  toggleTask(id) {
    const { done } = this.tasks.find((task) => task.id === id);
    this.updateTask(id, { done: !done });
  }

  removeTask(id) {
    this.tasks = this.tasks.filter((task) => task.id !== id);
    if (this.editingId === id) this.resetForm();
    this.commit();
  }

  // ----- Form & event -----
  bindEvents() {
    const { form, list, filters, cancel } = this.dom;

    form.addEventListener('submit', (event) => {
      event.preventDefault();
      this.handleSubmit();
    });
    cancel.addEventListener('click', () => this.resetForm());

    filters.addEventListener('click', ({ target }) => {
      const button = target.closest('[data-filter]');
      if (!button) return;
      this.filter = button.dataset.filter;
      this.render();
    });

    list.addEventListener('click', ({ target }) => {
      const button = target.closest('[data-action]');
      if (!button) return;
      const { action } = button.dataset;
      const { id } = button.closest('li').dataset;
      if (action === 'toggle') this.toggleTask(id);
      if (action === 'edit') this.startEdit(id);
      if (action === 'delete') this.removeTask(id);
    });
  }

  handleSubmit() {
    const { title, course, deadline } = Object.fromEntries(new FormData(this.dom.form));
    const data = { title: title.trim(), course: course.trim(), deadline };
    if (!data.title) return;

    if (this.editingId) this.updateTask(this.editingId, data);
    else this.addTask(data);
    this.resetForm();
  }

  startEdit(id) {
    const task = this.tasks.find((item) => item.id === id);
    if (!task) return;
    const { title, course, deadline } = this.dom.form.elements;
    title.value = task.title;
    course.value = task.course;
    deadline.value = task.deadline;
    this.editingId = id;
    this.dom.submit.textContent = 'Simpan perubahan';
    this.dom.cancel.hidden = false;
    title.focus();
  }

  resetForm() {
    this.dom.form.reset();
    this.editingId = null;
    this.dom.submit.textContent = 'Tambah tugas';
    this.dom.cancel.hidden = true;
  }

  // ----- Render (template literals) -----
  get visibleTasks() {
    const rules = { all: () => true, active: ({ done }) => !done, done: ({ done }) => done };
    return this.tasks
      .filter(rules[this.filter])
      .sort((a, b) => a.done - b.done || (a.deadline || '9999').localeCompare(b.deadline || '9999'));
  }

  taskTemplate = (task) => {
    const { id, title, course, deadline, done, urgency, statusLabel } = task;
    return `
      <li class="task ${urgency} ${done ? 'done' : ''}" data-id="${id}">
        <input type="checkbox" data-action="toggle" ${done ? 'checked' : ''}
          aria-label="Tandai selesai: ${escapeHtml(title)}">
        <div>
          <p class="task-title">${escapeHtml(title)}</p>
          <p class="task-meta">
            ${course ? `<span>${escapeHtml(course)}</span>` : ''}
            ${deadline ? `<span>${formatDate(deadline)}</span>` : ''}
            <strong>${statusLabel}</strong>
          </p>
        </div>
        <button type="button" class="ghost" data-action="edit">Ubah</button>
        <button type="button" class="ghost danger" data-action="delete">Hapus</button>
      </li>`;
  };

  render() {
    const { list, filters, statsText, statsBar } = this.dom;
    const visible = this.visibleTasks;
    const emptyText = this.tasks.length ? 'Tidak ada tugas di filter ini.' : 'Belum ada tugas. Tambahkan tugas pertamamu lewat form di atas.';

    list.innerHTML = visible.length ? visible.map(this.taskTemplate).join('') : `<li class="empty">${emptyText}</li>`;
    filters.querySelectorAll('[data-filter]').forEach((btn) =>
      btn.classList.toggle('active', btn.dataset.filter === this.filter));

    const total = this.tasks.length;
    const finished = this.tasks.filter(({ done }) => done).length;
    statsText.textContent = `${finished} dari ${total} tugas selesai`;
    statsBar.style.width = total ? `${(finished / total) * 100}%` : '0%';
  }

  // ----- Jam & sapaan -----
  startClock() {
    const { clock, date, greeting } = this.dom;
    const tick = () => {
      const now = new Date();
      const hour = now.getHours();
      clock.textContent = now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' }).replace('.', ':');
      date.textContent = now.toLocaleDateString('id-ID', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
      let sapaan = 'Selamat malam';
      if (hour < 11) sapaan = 'Selamat pagi';
      else if (hour < 15) sapaan = 'Selamat siang';
      else if (hour < 18) sapaan = 'Selamat sore';
      greeting.textContent = sapaan;
    };
    tick();
    setInterval(tick, 15_000);
  }

  // ----- Async/Await: data dari API publik -----
  async loadWeather() {
    const { weather } = this.dom;
    try {
      const response = await fetch(WEATHER_URL);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const { current_weather: { temperature, windspeed, weathercode } } = await response.json();
      weather.innerHTML = `
        <p class="big">${Math.round(temperature)}°C</p>
        <p>${describeWeather(weathercode)}, angin ${windspeed} km/jam</p>
        <p class="muted">Kampus ITERA, Lampung Selatan</p>`;
    } catch (error) {
      weather.textContent = 'Cuaca belum bisa dimuat. Periksa koneksi internetmu.';
    }
  }

  async loadQuote() {
    const { quote } = this.dom;
    try {
      const response = await fetch(QUOTE_URL);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const { quote: text, author } = await response.json();
      quote.innerHTML = `<q>${escapeHtml(text)}</q><cite>${escapeHtml(author)}</cite>`;
    } catch (error) {
      quote.textContent = 'Kerjakan satu tugas kecil dulu, sisanya akan terasa lebih ringan.';
    }
  }
}

new DashboardApp();
