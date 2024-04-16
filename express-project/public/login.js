document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    let response;

    try {
        response = await fetch('/users/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password })
        });
    } catch (error) {
        console.log('Falha na requisição:', error);
        document.getElementById('message').textContent = 'Falha ao conectar ao servidor.';
        return; 
    }

    if (response.ok) {
        const result = await response.json();
        document.getElementById('message').textContent = 'Login successful!';
    } else {
        const result = await response.json();
        document.getElementById('message').textContent = 'Error: ' + (result.Error || 'Failed to login.');
    }
});
