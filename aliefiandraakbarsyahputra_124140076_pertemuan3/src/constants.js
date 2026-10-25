// Status buku yang tersedia di aplikasi
export const STATUSES = [
  { value: 'milik', label: 'Dimiliki' },
  { value: 'baca', label: 'Sedang dibaca' },
  { value: 'beli', label: 'Ingin dibeli' },
];

export const statusLabel = (value) => STATUSES.find((s) => s.value === value)?.label ?? value;
