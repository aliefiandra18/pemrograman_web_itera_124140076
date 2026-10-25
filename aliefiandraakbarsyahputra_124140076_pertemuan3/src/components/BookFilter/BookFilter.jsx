import PropTypes from 'prop-types';
import { STATUSES } from '../../constants';
import './BookFilter.css';

const OPTIONS = [{ value: 'semua', label: 'Semua' }, ...STATUSES];

// Pencarian judul/penulis + filter status
function BookFilter({ status, query, onStatusChange, onQueryChange }) {
  return (
    <div className="filter">
      <label className="filter__search">
        <span>Cari judul atau penulis</span>
        <input type="search" value={query} onChange={(e) => onQueryChange(e.target.value)} />
      </label>
      <div className="filter__tabs" role="group" aria-label="Filter status">
        {OPTIONS.map((o) => (
          <button key={o.value} type="button" aria-pressed={status === o.value} onClick={() => onStatusChange(o.value)}>
            {o.label}
          </button>
        ))}
      </div>
    </div>
  );
}

BookFilter.propTypes = {
  status: PropTypes.string.isRequired,
  query: PropTypes.string.isRequired,
  onStatusChange: PropTypes.func.isRequired,
  onQueryChange: PropTypes.func.isRequired,
};

export default BookFilter;
