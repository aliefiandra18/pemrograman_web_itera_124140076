import { createContext, useCallback, useContext, useMemo, useState } from 'react';
import PropTypes from 'prop-types';
import { useLocalStorage } from '../hooks/useLocalStorage';

const BookContext = createContext(null);
const newId = () => `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;

// Provider: state global buku + filter + pencarian
export function BookProvider({ children }) {
  const [books, setBooks] = useLocalStorage('books', []);
  const [statusFilter, setStatusFilter] = useState('semua');
  const [query, setQuery] = useState('');

  const addBook = useCallback((data) => setBooks((prev) => [...prev, { id: newId(), ...data }]), [setBooks]);
  const updateBook = useCallback(
    (id, data) => setBooks((prev) => prev.map((b) => (b.id === id ? { ...b, ...data } : b))),
    [setBooks]
  );
  const deleteBook = useCallback((id) => setBooks((prev) => prev.filter((b) => b.id !== id)), [setBooks]);

  // Filter status + pencarian judul/penulis
  const filteredBooks = useMemo(() => {
    const q = query.trim().toLowerCase();
    return books.filter(
      (b) =>
        (statusFilter === 'semua' || b.status === statusFilter) &&
        (!q || b.title.toLowerCase().includes(q) || b.author.toLowerCase().includes(q))
    );
  }, [books, statusFilter, query]);

  const value = useMemo(
    () => ({ books, filteredBooks, statusFilter, setStatusFilter, query, setQuery, addBook, updateBook, deleteBook }),
    [books, filteredBooks, statusFilter, query, addBook, updateBook, deleteBook]
  );

  return <BookContext.Provider value={value}>{children}</BookContext.Provider>;
}
BookProvider.propTypes = { children: PropTypes.node.isRequired };

export function useBooks() {
  const ctx = useContext(BookContext);
  if (!ctx) throw new Error('useBooks harus dipakai di dalam BookProvider');
  return ctx;
}
