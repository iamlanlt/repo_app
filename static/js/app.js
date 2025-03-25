$(document).ready(function() {
    $('#searchBtn').click(function() {
      const username = $('#username').val().trim();
      if (!username) {
        alert('Please enter a GitHub username.');
        return;
      }

      $.ajax({
        url: `/get-repos/?username=${username}`,
        type: 'GET',
        success: function(data) {
          $('#repoList').empty();
          if (data.repos && data.repos.length > 0) {
            data.repos.forEach(repo => {
              $('#repoList').append(
                `<li class="list-group-item">
                  <a href="${repo.url}" target="_blank">${repo.name}</a>
                </li>`
              );
            });
          } else {
            $('#repoList').append('<li class="list-group-item">No repositories found.</li>');
          }
        },
        error: function(err) {
          const errorMsg = err.responseJSON ? err.responseJSON.error : 'An error occurred';
          alert(errorMsg);
        }
      });
    });
  });
