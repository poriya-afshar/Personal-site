    function toggleReplyForm(id) {
        const form = document.getElementById('reply-form-' + id);
        if (form.style.display === 'none' || form.style.display === '') {
            form.style.display = 'block';
        } else {
            form.style.display = 'none';
        }
    }