import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import BookFilter from '../components/BookFilter/BookFilter';
import BookList from '../components/BookList/BookList';

const books = [
  { id: '1', title: 'Bumi', author: 'Tere Liye', status: 'milik' },
  { id: '2', title: 'Laskar Pelangi', author: 'Andrea Hirata', status: 'baca' },
];

describe('BookFilter', () => {
  it('memanggil callback saat mengetik dan memilih status', () => {
    const onQueryChange = vi.fn();
    const onStatusChange = vi.fn();
    render(<BookFilter status="semua" query="" onStatusChange={onStatusChange} onQueryChange={onQueryChange} />);
    fireEvent.change(screen.getByLabelText(/cari judul/i), { target: { value: 'bumi' } });
    fireEvent.click(screen.getByRole('button', { name: 'Sedang dibaca' }));
    expect(onQueryChange).toHaveBeenCalledWith('bumi');
    expect(onStatusChange).toHaveBeenCalledWith('baca');
  });
});

describe('BookList', () => {
  it('menampilkan daftar buku', () => {
    render(<BookList books={books} onEdit={() => {}} onDelete={() => {}} />);
    expect(screen.getByText('Bumi')).toBeInTheDocument();
    expect(screen.getByText('Andrea Hirata')).toBeInTheDocument();
  });

  it('menampilkan pesan kosong', () => {
    render(<BookList books={[]} onEdit={() => {}} onDelete={() => {}} emptyMessage="Kosong" />);
    expect(screen.getByText('Kosong')).toBeInTheDocument();
  });

  it('meminta konfirmasi sebelum menghapus', () => {
    const onDelete = vi.fn();
    render(<BookList books={books} onEdit={() => {}} onDelete={onDelete} />);
    fireEvent.click(screen.getByRole('button', { name: 'Hapus Bumi' }));
    expect(onDelete).not.toHaveBeenCalled();
    fireEvent.click(screen.getByRole('button', { name: 'Ya, hapus' }));
    expect(onDelete).toHaveBeenCalledWith('1');
  });
});
