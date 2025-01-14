document.addEventListener('DOMContentLoaded', function () {
    const copyButton = document.getElementById('copyLinkButton'); // Copy button
    const previewButton = document.getElementById('previewButton'); // Preview button

    if (copyButton && previewButton) {
        copyButton.addEventListener('click', function () {
            const baseURL = window.location.origin;
            const relativeURL = previewButton.getAttribute('href');
            const uniqueLink = `${baseURL}${relativeURL}`;

            navigator.clipboard.writeText(uniqueLink).then(() => {
                alert('Unique link copied to clipboard!');
            }).catch(err => {
                alert('Failed to copy the link. Please try again.');
                console.error(err);
            });
        });
    } else {
        console.log("Copy button or preview button not found on this page.");
    }
});
