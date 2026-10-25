import { useState } from 'react';
import PropTypes from 'prop-types';
import { statusLabel } from '../../constants';
import './BookList.css';

const bookShape = PropTypes.shape({
  id: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  author: PropTypes.string.isRequired,
  status: PropTypes.oneOf(['milik', 'baca', 'beli']).isRequired,
});

// Satu baris buku; hapus memakai konfirmasi inline
function BookItem({ book, onEdit, onDelete }) {
  const [confirming, setConfirming] = useState(false);
  return (
    <li className={`book book--${book.status}`}>
      <div className="book__info">
        <h3>{book.title}</h3>
        <p>{book.author}</p>
      </div>
      <span className="book__status">{statusLabel(book.status)}</span>
      <div className="book__actions">
        {confirming ? (
          <>
            <button type="button" className="btn btn--danger" onClick={() => onDelete(book.id)}>
              Ya, hapus
            </button>
            <button type="button" className="btn" onClick={() => setConfirming(false)}>
              Batal
            </button>
          </>
        ) : (
          <>
            <button type="button" className="btn" aria-label={`Edit ${book.title}`} onClick={() => onEdit(book)}>
              Edit
            </button>
            <button type="button" className="btn" aria-label={`Hapus ${book.title}`} onClick={() => setConfirming(true)}>
              Hapus
            </button>
          </>
        )}
      </div>
    </li>
  );
}
BookItem.propTypes = { book: bookShape.isRequired, onEdit: PropTypes.func.isRequired, onDelete: PropTypes.func.isRequired };

// Daftar buku (atau pesan kosong)
function BookList({ books, onEdit, onDelete, emptyMessage = 'Belum ada buku.' }) {
  if (books.length === 0) return <p className="book-empty">{emptyMessage}</p>;
  return (
    <ul className="book-list">
      {books.map((b) => (
        <BookItem key={b.id} book={b} onEdit={onEdit} onDelete={onDelete} />
      ))}
    </ul>
  );
}

BookList.propTypes = {
  books: PropTypes.arrayOf(bookShape).isRequired,
  onEdit: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
  emptyMessage: PropTypes.string,
};

export default BookList;
