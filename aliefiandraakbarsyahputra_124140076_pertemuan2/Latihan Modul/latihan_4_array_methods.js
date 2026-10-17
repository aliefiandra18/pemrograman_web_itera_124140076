// Latihan 4: Modern Array Methods

// 1. Fungsi groupBy menggunakan reduce()
const groupBy = (array, property) => {
  return array.reduce((acc, obj) => {
    const key = obj[property];
    if (!acc[key]) acc[key] = [];
    acc[key].push(obj);
    return acc;
  }, {});
};
const dataSiswa = [
  { nama: "Andi", kelas: "A" }, { nama: "Budi", kelas: "B" }, { nama: "Caca", kelas: "A" }
];
console.log("Group By Kelas:", !!groupBy(dataSiswa, 'kelas') ? "Berhasil" : "Gagal");

// 2. Menghitung rata-rata dari array of objects
const hitungRataRata = (arr, key) => {
  if (arr.length === 0) return 0;
  const total = arr.reduce((sum, obj) => sum + obj[key], 0);
  return total / arr.length;
};
const nilai = [{ skor: 80 }, { skor: 90 }, { skor: 100 }];
console.log("Rata-rata Skor:", hitungRataRata(nilai, 'skor'));

// 3. Transform struktur array bersarang menjadi flat
const arrayBersarang = [1, [2, 3], [[4, 5], 6]];
const flattenDeep = (arr) => {
  return arr.reduce((acc, val) => 
    Array.isArray(val) ? [...acc, ...flattenDeep(val)] : [...acc, val], []
  );
};
console.log("Array Datar:", flattenDeep(arrayBersarang));

// 4. Gabungkan filter, map, reduce untuk analisis
const transaksi = [
  { id: 1, type: 'income', amount: 50000 },
  { id: 2, type: 'expense', amount: 20000 },
  { id: 3, type: 'income', amount: 75000 }
];
// Hitung total income
const totalIncome = transaksi
  .filter(trx => trx.type === 'income')
  .map(trx => trx.amount)
  .reduce((acc, amount) => acc + amount, 0);
console.log("Total Income:", totalIncome);
