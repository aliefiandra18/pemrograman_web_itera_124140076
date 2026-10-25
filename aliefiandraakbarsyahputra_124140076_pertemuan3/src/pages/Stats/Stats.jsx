import { STATUSES } from '../../constants';
import { useBooks } from '../../context/BookContext';
import { useBookStats } from '../../hooks/useBookStats';

// Halaman statistik koleksi
export default function Stats() {
  const { books } = useBooks();
  const { total, counts, percent } = useBookStats(books);
  return (
    <section>
      <h2>Statistik koleksi</h2>
      <p>
        Total <strong>{total}</strong> buku tercatat.
      </p>
      <ul className="stats">
        {STATUSES.map((s) => (
          <li key={s.value} className={`stat stat--${s.value}`}>
            <span>{s.label}</span>
            <strong>{counts[s.value]}</strong>
            <div className="stat__bar" aria-hidden="true">
              <div style={{ width: `${percent[s.value]}%` }} />
            </div>
          </li>
        ))}
      </ul>
    </section>
  );
}
