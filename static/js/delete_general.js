function eliminarEmail(id) {
  if (confirm('¿Estás seguro de que deseas eliminar este usuario?')) {
    fetch(`${window.origin}/Eliminar/${id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      
      }
    })
    .then(response => {
      if (response.ok) {
        // Recargar la página o redirigir a la página de administración después de eliminar el usuario
        window.location.reload();
        // O bien: window.location.href = '{{ url_for("ruta.admin") }}';
      } else {
        alert('Hubo un error al eliminar el usuario.');
      }
    })
    .catch(error => {
      alert('Hubo un error al eliminar el usuario.');
    });
  }
}

function eliminarEmpleado(id) {
  if (confirm('¿Estás seguro de que deseas eliminar este usuario?')) {
    fetch(`${window.origin}/Eliminarempleado/${id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      
      }
    })
    .then(response => {
      if (response.ok) {
        // Recargar la página o redirigir a la página de administración después de eliminar el usuario
        window.location.reload();
        // O bien: window.location.href = '{{ url_for("ruta.admin") }}';
      } else {
        alert('Hubo un error al eliminar el usuario.');
      }
    })
    .catch(error => {
      alert('Hubo un error al eliminar el usuario.');
    });
  }
}

function eliminarBitacora(id) {
  if (confirm('¿Estás seguro de que deseas eliminar este usuario?')) {
    fetch(`${window.origin}/Eliminarbitacora/${id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      
      }
    })
    .then(response => {
      if (response.ok) {
        // Recargar la página o redirigir a la página de administración después de eliminar el usuario
        window.location.reload();
        // O bien: window.location.href = '{{ url_for("ruta.admin") }}';
      } else {
        alert('Hubo un error al eliminar el usuario.');
      }
    })
    .catch(error => {
      alert('Hubo un error al eliminar el usuario.');
    });
  }
}