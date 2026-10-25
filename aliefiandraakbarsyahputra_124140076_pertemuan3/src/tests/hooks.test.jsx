import { act, renderHook } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { useLocalStorage } from '../hooks/useLocalStorage';
import { useBookStats } from '../hooks/useBookStats';

describe('useLocalStorage', () => {
  it('membaca nilai awal dari localStorage', () => {
    localStorage.setItem('k', JSON.stringify([1]));
    const { result } = renderHook(() => useLocalStorage('k', []));
    expect(result.current[0]).toEqual([1]);
  });

  it('menyimpan perubahan ke localStorage', () => {
    const { result } = renderHook(() => useLocalStorage('k2', []));
    act(() => result.current[1]([1, 2]));
    expect(JSON.parse(localStorage.getItem('k2'))).toEqual([1, 2]);
  });
});

describe('useBookStats', () => {
  it('menghitung total, jumlah per status, dan persentase', () => {
    const books = [{ status: 'milik' }, { status: 'milik' }, { status: 'baca' }, { status: 'beli' }];
    const { result } = renderHook(() => useBookStats(books));
    expect(result.current.total).toBe(4);
    expect(result.current.counts).toEqual({ milik: 2, baca: 1, beli: 1 });
    expect(result.current.percent.milik).toBe(50);
  });
});
