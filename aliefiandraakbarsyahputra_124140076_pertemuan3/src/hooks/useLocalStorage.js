import { useState, useEffect } from 'react';

// Custom hook #1: state yang otomatis tersimpan di localStorage
export function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const raw = localStorage.getItem(key);
      return raw !== null ? JSON.parse(raw) : initialValue;
    } catch {
      return initialValue; // data rusak / localStorage diblokir
    }
  });

  // Simpan ulang setiap kali value berubah
  useEffect(() => {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch {
      /* penyimpanan penuh atau diblokir: abaikan */
    }
  }, [key, value]);

  return [value, setValue];
}
