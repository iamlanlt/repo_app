$(document).ready(function() {
  $('#search').click(function() {
    const username = $('#username').val().trim();
    $('#result').html('');

    if (!username) {
      $('#result').html('<div class="alert alert-danger">Please enter a GitHub username.</div>');
      return;
    }

    $('#result').html('<div class="text-center my-4"><div class="spinner-border text-primary" role="status"></div> <p>Loading...</p></div>');

    $.ajax({
      url: '/get-repos/',
      method: 'GET',
      data: { username: username },
      success: function(response) {
        if (response.repos.length === 0) {
          $('#result').html('<div class="alert alert-warning">No repositories found for this user.</div>');
          return;
        }

        const repoList = response.repos.map(repo => `
          <div class="repo-card">
            <h3><a href="${repo.url}" target="_blank">${repo.name}</a></h3>
            <p>${repo.description || 'No description available.'}</p>
            <p>
              <span class="badge bg-primary">⭐ Stars: ${repo.stars}</span>
              <span class="badge bg-success">🍴 Forks: ${repo.forks}</span>
              <span class="badge bg-info">🛠 Language: ${repo.languages}</span>
            </p>
            <p class="text-muted">📅 Created: ${repo.created_at} | Updated: ${repo.updated_at}</p>
          </div>
        `).join('');

        $('#result').html(repoList);
      },
      error: function(response) {
        $('#result').html(`<div class="alert alert-danger">${response.responseJSON.error}</div>`);
      }
    });
  });
});
