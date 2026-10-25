import { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import { STATUSES } from '../../constants';
import './BookForm.css';

const EMPTY = { title: '', author: '', status: 'milik' };

// Validasi kolom wajib isi
export function validate(v) {
  const errors = {};
  if (!v.title.trim()) errors.title = 'Judul wajib diisi';
  if (!v.author.trim()) errors.author = 'Penulis wajib diisi';
  return errors;
}

// Form tambah/edit buku (mode edit aktif jika initialValues diberikan)
function BookForm({ initialValues, onSubmit, onCancel }) {
  const [values, setValues] = useState(initialValues || EMPTY);
  const [errors, setErrors] = useState({});
  const editing = Boolean(initialValues);

  // Sinkronkan isi form saat buku yang diedit berganti
  useEffect(() => {
    setValues(initialValues || EMPTY);
    setErrors({});
  }, [initialValues]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setValues((v) => ({ ...v, [name]: value }));
    if (errors[name]) setErrors((er) => ({ ...er, [name]: undefined }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const found = validate(values);
    setErrors(found);
    if (Object.keys(found).length > 0) return;
    onSubmit({ title: values.title.trim(), author: values.author.trim(), status: values.status });
    if (!editing) setValues(EMPTY);
  };

  const textField = (name, label) => (
    <div className="field">
      <label htmlFor={name}>{label}</label>
      <input
        id={name}
        name={name}
        value={values[name]}
        onChange={handleChange}
        className={errors[name] ? 'input-error' : ''}
        aria-invalid={Boolean(errors[name])}
        aria-describedby={errors[name] ? `${name}-error` : undefined}
      />
      {errors[name] && (
        <p id={`${name}-error`} className="field-error" role="alert">
          {errors[name]}
        </p>
      )}
    </div>
  );

  return (
    <form className="book-form" onSubmit={handleSubmit} noValidate>
      {textField('title', 'Judul')}
      {textField('author', 'Penulis')}
      <div className="field">
        <label htmlFor="status">Status</label>
        <select id="status" name="status" value={values.status} onChange={handleChange}>
          {STATUSES.map((s) => (
            <option key={s.value} value={s.value}>
              {s.label}
            </option>
          ))}
        </select>
      </div>
      <div className="book-form__actions">
        <button type="submit" className="btn btn--primary">
          {editing ? 'Simpan perubahan' : 'Tambah buku'}
        </button>
        {onCancel && (
          <button type="button" className="btn" onClick={onCancel}>
            Batal
          </button>
        )}
      </div>
    </form>
  );
}

BookForm.propTypes = {
  initialValues: PropTypes.shape({
    title: PropTypes.string,
    author: PropTypes.string,
    status: PropTypes.oneOf(['milik', 'baca', 'beli']),
  }),
  onSubmit: PropTypes.func.isRequired,
  onCancel: PropTypes.func,
};

export default BookForm;
