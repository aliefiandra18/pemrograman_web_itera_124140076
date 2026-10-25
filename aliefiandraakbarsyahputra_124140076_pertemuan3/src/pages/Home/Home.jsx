import { useState } from 'react';
import BookForm from '../../components/BookForm/BookForm';
import BookFilter from '../../components/BookFilter/BookFilter';
import BookList from '../../components/BookList/BookList';
import { useBooks } from '../../context/BookContext';

// Halaman utama: form tambah/edit + filter + daftar buku
export default function Home() {
  const { books, filteredBooks, statusFilter, setStatusFilter, query, setQuery, addBook, updateBook, deleteBook } = useBooks();
  const [editing, setEditing] = useState(null);

  const handleSubmit = (data) => {
    if (editing) {
      updateBook(editing.id, data);
      setEditing(null);
    } else {
      addBook(data);
    }
  };

  const handleDelete = (id) => {
    deleteBook(id);
    if (editing?.id === id) setEditing(null);
  };

  const emptyMessage = books.length === 0 ? 'Belum ada buku. Tambahkan buku pertamamu lewat form.' : 'Tidak ada buku yang cocok dengan filter atau pencarian.';

  return (
    <div className="home">
      <section className="panel">
        <h2>{editing ? 'Edit buku' : 'Tambah buku'}</h2>
        <BookForm initialValues={editing} onSubmit={handleSubmit} onCancel={editing ? () => setEditing(null) : undefined} />
      </section>
      <section>
        <BookFilter status={statusFilter} query={query} onStatusChange={setStatusFilter} onQueryChange={setQuery} />
        <BookList books={filteredBooks} onEdit={setEditing} onDelete={handleDelete} emptyMessage={emptyMessage} />
      </section>
    </div>
  );
}
