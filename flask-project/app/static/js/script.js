document.getElementById('addMovieForm').onsubmit = function(e) {
    e.preventDefault();
    console.log("aqui")
    const formData = {
        name: document.getElementById('name').value,
        description: document.getElementById('description').value,
        release_date: document.getElementById('release_date').value,
        director: document.getElementById('director').value,
        genre: document.getElementById('genre').value
    };

    fetch('/movie/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    }).then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Algo errado aconteceu!');
    }).then(data => {
        window.location.reload();
    }).catch(error => {
        console.error('Error:', error);
    });
};

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('#deleteMovieForm').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault(); 
            const movieId = this.querySelector('#movie_id').value;

            fetch(`/movie/delete/${movieId}`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                }    
            }).then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Algo errado aconteceu!');
            }).then(data => {
                console.log('Filme deletado:', data);
                window.location.reload();
            }).catch(error => {
                console.error('Error:', error);
            });
        });
    });
});
