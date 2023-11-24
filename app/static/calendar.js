const emotions = [
    '/emotions/angry.png',
    '/emotions/annoyed.png',
    '/emotions/down.png',
    '/emotions/frustrated.png',
    '/emotions/happy.png',
    '/emotions/loved.png',
    '/emotions/proud.png',
    '/emotions/sad.png',
    '/emotions/scared.png',
    '/emotions/shy.png',
    '/emotions/sleepy.png',
    '/emotions/stressed.png',
    '/emotions/surprised.png',
    '/emotions/worried.png'
];

(() => {
    const show_modal = (selected_date) => {
        const modal = document.createElement('div');
        modal.className = 'modal';
        console.log(selected_date);

        const selectedImagesContainer = document.createElement('div');
        selectedImagesContainer.className = 'selected-images-container';

        emotions.forEach((emotionUrl, index) => {
            const emotionImage = document.createElement('img');
            emotionImage.src = emotionUrl;
            emotionImage.alt = `Émotion ${index + 1}`;
            emotionImage.className = 'emotion-image';

            emotionImage.addEventListener('click', async () => {
                const selectedEmotion = emotionUrl;

                await json_fetch('/emotion', { method: 'POST', body: JSON.stringify({ date: selected_date, emotion: selectedEmotion }) });

                update_mood_img(selected_date, selectedEmotion, selectedImagesContainer);
                modal.remove();
            });

            selectedImagesContainer.appendChild(emotionImage);
        });

        modal.appendChild(selectedImagesContainer);
        document.body.appendChild(modal);
    };

    const update_mood_img = (date, emotionUrl) => {
        const day_cell = document.querySelector(`td[data-date="${date}"]`);
        if (!day_cell)
            return;

        day_cell.querySelector('img').src = emotionUrl;
    };

    document.querySelectorAll('td.mood-section > button').forEach((btn) => {
        btn.addEventListener('click', () => {
            const selected_date = btn.closest('td').dataset.date;
            show_modal(selected_date);
        });
    });
})();
