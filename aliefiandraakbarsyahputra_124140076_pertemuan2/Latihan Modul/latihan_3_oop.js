// Latihan 3: Classes & Object Literals

// 1 & 2. Class Product (Inheritance) dan Implementasi Getter/Setter
class Product {
  constructor(nama, hargaDasar) {
    this.nama = nama;
    this.hargaDasar = hargaDasar;
    this._diskon = 0; // Private property convention
  }
  
  // Setter
  set diskon(persen) {
    if (persen >= 0 && persen <= 100) {
      this._diskon = persen;
    }
  }
  
  // Getter
  get hargaAkhir() {
    return this.hargaDasar - (this.hargaDasar * (this._diskon / 100));
  }
}

class DigitalProduct extends Product {
  constructor(nama, hargaDasar, ukuranMB) {
    super(nama, hargaDasar);
    this.ukuranMB = ukuranMB;
  }
}

class PhysicalProduct extends Product {
  constructor(nama, hargaDasar, beratKg) {
    super(nama, hargaDasar);
    this.beratKg = beratKg;
  }
}

// 3. Computed property names (Dynamic keys)
const prefix = "item";
const idUnik = 123;
const dynamicObj = {
  [`${prefix}_${idUnik}`]: "Laptop Gaming",
  [`is_available`]: true
};
console.log("Dynamic Object:", dynamicObj);

// 4. Combine default parameters dengan destructuring
const setupConfig = ({ host = "localhost", port = 8080, secure = false } = {}) => {
  const protocol = secure ? "https" : "http";
  console.log(`Server URL: ${protocol}://${host}:${port}`);
};
setupConfig(); // Menggunakan semua default
setupConfig({ port: 3000, secure: true }); // Override sebagian
