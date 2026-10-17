// Latihan 1: Let, Const, Arrow Functions, Template Literals

// 1. Coba ubah nilai const dan lihat error
const bootcamp = "PAW";
// bootcamp = "Web"; // Jika di-uncomment, akan menghasilkan TypeError: Assignment to constant variable.

// 2. Bandingkan behavior var di dalam dan luar block
var namaVar = "Luar";
{
  var namaVar = "Dalam";
}
console.log("var:", namaVar); // Output: "Dalam" (Data bocor ke luar blok)

let namaLet = "Luar";
{
  let namaLet = "Dalam";
}
console.log("let:", namaLet); // Output: "Luar" (Aman, tidak terpengaruh blok dalam)

// 3. Buat arrow function dengan berbagai sintaks
const sapa = () => "Halo!"; // Tanpa parameter
const kuadrat = x => x * x; // Satu parameter
const tambah = (a, b) => a + b; // Dua parameter

// 4. Gunakan template literals untuk membuat HTML string
const htmlString = `
  <div class="card">
    <h1>${sapa()}</h1>
    <p>2 kuadrat adalah ${kuadrat(2)}</p>
  </div>
`;
console.log(htmlString);
