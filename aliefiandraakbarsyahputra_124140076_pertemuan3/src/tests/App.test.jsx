import { fireEvent, render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { describe, expect, it } from 'vitest';
import App from '../App';
import { BookProvider } from '../context/BookContext';

const renderApp = () =>
  render(
    <MemoryRouter>
      <BookProvider>
        <App />
      </BookProvider>
    </MemoryRouter>
  );

const addBook = (title, author, status = 'milik') => {
  fireEvent.change(screen.getByLabelText('Judul'), { target: { value: title } });
  fireEvent.change(screen.getByLabelText('Penulis'), { target: { value: author } });
  fireEvent.change(screen.getByLabelText('Status'), { target: { value: status } });
  fireEvent.click(screen.getByRole('button', { name: 'Tambah buku' }));
};

describe('App (integrasi)', () => {
  it('menambah buku, mencari, dan menyimpannya ke localStorage', () => {
    renderApp();
    addBook('Bumi', 'Tere Liye');
    addBook('Laskar Pelangi', 'Andrea Hirata', 'baca');
    expect(screen.getByText('Bumi')).toBeInTheDocument();
    expect(JSON.parse(localStorage.getItem('books'))).toHaveLength(2);

    fireEvent.change(screen.getByLabelText(/cari judul/i), { target: { value: 'andrea' } });
    expect(screen.queryByText('Bumi')).not.toBeInTheDocument();
    expect(screen.getByText('Laskar Pelangi')).toBeInTheDocument();
  });

  it('berpindah ke halaman statistik', () => {
    renderApp();
    addBook('Bumi', 'Tere Liye');
    fireEvent.click(screen.getByRole('link', { name: 'Statistik' }));
    expect(screen.getByText('Statistik koleksi')).toBeInTheDocument();
  });
});
