// Latihan 5: Async Programming (Promises & Async/Await)

// Memodelkan sebuah fungsi asinkron (mengganti request API)
const ambilDataServer = (sukses = true) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (sukses) {
        resolve({ status: 200, message: "Data berhasil diunduh!" });
      } else {
        reject(new Error("Koneksi ke server terputus."));
      }
    }, 1500); // Simulasi delay 1.5 detik
  });
};

// Menggunakan metode Async/Await
const jalankanAplikasi = async () => {
  console.log("Sedang mengambil data...");
  try {
    const hasil = await ambilDataServer(true);
    console.log("Berhasil:", hasil.message);
  } catch (error) {
    console.error("Gagal:", error.message);
  } finally {
    console.log("Proses fetch selesai (Cleanup dijalankan).");
  }
};

jalankanAplikasi();
