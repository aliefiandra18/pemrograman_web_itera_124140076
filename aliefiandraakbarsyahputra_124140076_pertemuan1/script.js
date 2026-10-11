// ==========================================
// INISIALISASI STATE & VARIABEL GLOBAL
// ==========================================
// Mengambil data dari localStorage jika ada, jika kosong gunakan array []
let cart = JSON.parse(localStorage.getItem('cartData')) || [];
let totalAkhirBayar = 0; // State untuk menyimpan total akhir yang harus dibayar

// Menangkap Elemen DOM
const formElements = {
    nama: document.getElementById('inputNama'),
    harga: document.getElementById('inputHarga'), 
    qty: document.getElementById('inputQty'),
    btnTambah: document.getElementById('btnTambah'),
    errNama: document.getElementById('errNama'),
    errHarga: document.getElementById('errHarga'),
    errQty: document.getElementById('errQty')
};

const cartElements = {
    body: document.getElementById('cartBody'),
    totalBelanja: document.getElementById('txtTotalBelanja'),
    diskon: document.getElementById('txtDiskon'),
    totalAkhir: document.getElementById('txtTotalAkhir')
};

const payElements = {
    input: document.getElementById('inputBayar'),
    msg: document.getElementById('msgBayar'),
    kembalian: document.getElementById('txtKembalian'),
    btnReset: document.getElementById('btnReset')
};

// ==========================================
// UTILITY FUNCTIONS
// ==========================================
// Format angka ke format Rupiah standar Indonesia
const formatRupiah = (number) => {
    return new Intl.NumberFormat('id-ID', {
        style: 'currency',
        currency: 'IDR',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(number);
};

// ==========================================
// LOGIKA KERANJANG & KALKULATOR
// ==========================================
function renderCart() {
    cartElements.body.innerHTML = '';
    let totalBelanja = 0;

    // Render per baris tabel
    if (cart.length === 0) {
        cartElements.body.innerHTML = `
            <tr>
                <td colspan="6" class="text-center p-6 text-gray-500 italic">
                    Keranjang belanja masih kosong.
                </td>
            </tr>`;
    } else {
        cart.forEach((item, index) => {
            const subtotal = item.harga * item.qty;
            totalBelanja += subtotal;

            const tr = document.createElement('tr');
            tr.className = "hover:bg-gray-50 transition duration-150";
            tr.innerHTML = `
                <td class="p-3">${index + 1}</td>
                <td class="p-3 font-semibold">${item.nama}</td>
                <td class="p-3">${formatRupiah(item.harga)}</td>
                <td class="p-3 text-center">${item.qty}</td>
                <td class="p-3 font-semibold text-gray-700">${formatRupiah(subtotal)}</td>
                <td class="p-3 text-center">
                    <button onclick="hapusBarang(${item.id})" class="bg-red-100 text-red-600 px-3 py-1 rounded hover:bg-red-600 hover:text-white transition text-sm font-bold">
                        Hapus
                    </button>
                </td>
            `;
            cartElements.body.appendChild(tr);
        });
    }

    // Hitung Diskon (10% jika belanja >= Rp 50.000)
    let diskon = 0;
    if (totalBelanja >= 50000) {
        diskon = totalBelanja * 0.10;
    }
    
    totalAkhirBayar = totalBelanja - diskon;

    // Update DOM teks ringkasan
    cartElements.totalBelanja.innerText = formatRupiah(totalBelanja);
    cartElements.diskon.innerText = `- ${formatRupiah(diskon)}`;
    cartElements.totalAkhir.innerText = formatRupiah(totalAkhirBayar);

    // Simpan ke LocalStorage agar persisten
    localStorage.setItem('cartData', JSON.stringify(cart));

    // Picu hitung kembalian ulang otomatis setiap keranjang berubah
    hitungKembalian();
}

function hapusBarang(idTarget) {
    // Filter array: buang item yang ID-nya sama dengan idTarget
    cart = cart.filter(item => item.id !== idTarget);
    renderCart();
}

// ==========================================
// EVENT LISTENERS & VALIDASI FORM
// ==========================================
formElements.btnTambah.addEventListener('click', () => {
    // Ambil nilai dari input
    const nama = formElements.nama.value.trim();
    const harga = parseFloat(formElements.harga.value);
    const qty = parseInt(formElements.qty.value);

    let isFormValid = true;

    // Validasi 1: Nama Barang (Min 3 karakter)
    if (nama.length < 3) {
        formElements.errNama.classList.remove('hidden');
        isFormValid = false;
    } else {
        formElements.errNama.classList.add('hidden');
    }

    // Validasi 2: Harga (Wajib positif, Min Rp 500)
    if (isNaN(harga) || harga < 500) {
        formElements.errHarga.classList.remove('hidden');
        isFormValid = false;
    } else {
        formElements.errHarga.classList.add('hidden');
    }

    // Validasi 3: Qty (Wajib angka bulat, Min 1)
    if (isNaN(qty) || qty < 1) {
        formElements.errQty.classList.remove('hidden');
        isFormValid = false;
    } else {
        formElements.errQty.classList.add('hidden');
    }

    // Jika semua valid, masukkan ke array keranjang
    if (isFormValid) {
        const newItem = {
            id: Date.now(), // Unique ID menggunakan timestamp
            nama: nama,
            harga: harga,
            qty: qty
        };
        
        cart.push(newItem);
        renderCart();

        // Reset form setelah berhasil
        formElements.nama.value = '';
        formElements.harga.value = '';
        formElements.qty.value = '1';
        
        // Fokuskan kembali ke input nama
        formElements.nama.focus();
    }
});

// ==========================================
// LOGIKA PEMBAYARAN & KEMBALIAN
// ==========================================
function hitungKembalian() {
    const bayar = parseFloat(payElements.input.value);

    // Jika input kosong atau keranjang kosong
    if (isNaN(bayar) || cart.length === 0) {
        payElements.msg.innerText = '';
        payElements.kembalian.innerText = 'Rp 0';
        return;
    }

    if (bayar < totalAkhirBayar) {
        payElements.msg.innerText = '❌ Uang belum mencukupi!';
        payElements.msg.className = 'text-sm mt-1 text-red-500 font-bold';
        payElements.kembalian.innerText = 'Rp 0';
    } else {
        const kembalian = bayar - totalAkhirBayar;
        payElements.msg.innerText = '✅ Uang cukup.';
        payElements.msg.className = 'text-sm mt-1 text-green-600 font-bold';
        payElements.kembalian.innerText = formatRupiah(kembalian);
    }
}

// Event otomatis hitung saat kasir mengetik angka
payElements.input.addEventListener('input', hitungKembalian);

// Tombol Reset / Transaksi Baru
payElements.btnReset.addEventListener('click', () => {
    if (cart.length === 0) return alert("Keranjang sudah kosong!");
    
    if (confirm("Apakah transaksi sudah selesai? Keranjang akan dikosongkan.")) {
        // Kosongkan array
        cart = [];
        
        // Hapus dari memory lokal
        localStorage.removeItem('cartData');
        
        // Reset input bayar
        payElements.input.value = '';
        
        // Render ulang DOM
        renderCart();
    }
});

// ==========================================
// RENDER PERTAMA SAAT HALAMAN DIMUAT
// ==========================================
renderCart();
