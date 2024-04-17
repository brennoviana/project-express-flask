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
        throw new Error('Something went wrong');
    }).then(data => {
        console.log('Filme adicionado:', data);
        window.location.reload();
    }).catch(error => {
        console.error('Error:', error);
    });
};