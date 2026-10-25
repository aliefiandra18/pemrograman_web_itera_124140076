import { useMemo } from 'react';

// Custom hook #2: menghitung statistik koleksi buku
export function useBookStats(books) {
  return useMemo(() => {
    const total = books.length;
    const counts = { milik: 0, baca: 0, beli: 0 };
    books.forEach((b) => {
      if (b.status in counts) counts[b.status] += 1;
    });
    const percent = Object.fromEntries(
      Object.entries(counts).map(([k, v]) => [k, total ? Math.round((v / total) * 100) : 0])
    );
    return { total, counts, percent };
  }, [books]);
}
