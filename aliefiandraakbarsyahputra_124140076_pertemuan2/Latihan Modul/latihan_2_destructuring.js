// Latihan 2: Destructuring & Operators

// 1. Destructure object dengan nested properties minimal 3 level
const dataUser = {
  user: {
    profile: {
      details: { id: 1, role: "admin", aktif: true }
    }
  }
};
const { user: { profile: { details: { id, role, aktif } } } } = dataUser;
console.log(`ID: ${id}, Role: ${role}, Aktif: ${aktif}`);

// 2. Function rest parameters untuk statistik (min, max, average)
const getStats = (...numbers) => {
  if (numbers.length === 0) return { min: 0, max: 0, avg: 0 };
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  const avg = numbers.reduce((a, b) => a + b, 0) / numbers.length;
  return { min, max, avg };
};
console.log("Statistik:", getStats(10, 20, 30, 40, 50));

// 3. Merge 3 objects dengan spread operator dan override
const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const obj3 = { b: 99, e: 5 }; // 'b' akan melakukan override pada obj1
const mergedObj = { ...obj1, ...obj2, ...obj3 };
console.log("Merged Object:", mergedObj);

// 4. Destructuring dalam loop for...of
const koordinat = [{ x: 10, y: 20 }, { x: 30, y: 40 }];
for (const { x, y } of koordinat) {
  console.log(`Koordinat X: ${x}, Y: ${y}`);
}
