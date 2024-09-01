document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', function() {
        const content = this.nextElementSibling;
        content.classList.toggle('active');
    });
});