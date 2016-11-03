$(document).ready(() => {
    $("#commentButton").click(function() {
        $("#commentForm").toggle();
        $("commentLineBreak").toggle();
    });
});


$(document).on('submit', '#commentForm', (e) => {
    e.preventDefault();
    const topic_id = $('input[name=topicid]').val();
    const topic_slug = $('input[name=topicslug]').val();
    const comment = $('#id_body').val();
    $.ajax({
        type: 'POST',
        url: '/topics/' + topic_slug + '/add/',
        data: {
            topic_id: topic_id,
            topic_slug: topic_id,
            comment: comment,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (res) {
            const resObject = JSON.parse(res);
            const comment = resObject.comment
            const type = resObject.type
            const user = resObject.user

            commentsList = document.getElementById('commentsList');

            const commentDiv = document.createElement('DIV');
            commentDiv.className = 'comment';

            const commentHeader = document.createElement('DIV');
            commentHeader.className = 'large-2 columns small-3';

            const userImg = document.createElement('IMG');
            userImg.setAttribute('src', 'http://placehold.it/50x50&text=[img]')
            const commentBody = document.createElement('DIV');
            commentBody.className = 'large-10 columns'

            const commentUser = document.createElement('P');
            commentUser.setAttribute('style', 'color: blue;');
            commentUser.innerHTML = user

            const commentText = document.createElement('P');
            commentText.innerHTML = comment

            const hr = document.createElement('HR');

            commentHeader.appendChild(userImg);
            commentDiv.appendChild(commentHeader);
            commentBody.appendChild(commentUser);
            commentBody.appendChild(commentText);
            commentDiv.appendChild(commentBody);
            commentDiv.appendChild(hr);

            commentsList.insertBefore(commentDiv, commentsList.firstChild);
        }
    })
})
