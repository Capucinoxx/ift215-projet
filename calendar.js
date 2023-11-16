let emotions = [
    '/emotions/Angry.PNG',
    '/emotions/Annoyed.PNG',
    '/emotions/Down.PNG',
    '/emotions/Frustrated.PNG',
    '/emotions/Happy.PNG',
    '/emotions/Loved.PNG',
    '/emotions/Proud.PNG',
    '/emotions/Sad.PNG',
    '/emotions/Scared.PNG',
    '/emotions/Shy.PNG',
    '/emotions/Sleepy.PNG',
    '/emotions/Stressed.PNG',
    '/emotions/Suprised.PNG',
    '/emotions/Worried.PNG'
];

function setInitialWeek() {
    const currentDate = new Date();
    const currentDayOfWeek = currentDate.getDay();
    currentWeekStart = new Date(currentDate);
    currentWeekStart.setDate(currentDate.getDate() - currentDayOfWeek);
}

function showEmotionSelector(currentDate) {
    const modal = document.createElement('div');
    modal.className = 'modal';

    const selectedImagesContainer = document.createElement('div');
    selectedImagesContainer.className = 'selected-images-container';

    emotions.forEach((emotionUrl, index) => {
        const emotionImage = document.createElement('img');
        emotionImage.src = emotionUrl;
        emotionImage.alt = `Émotion ${index + 1}`;
        emotionImage.className = 'emotion-image';

        emotionImage.addEventListener('click', () => {
            const selectedEmotion = emotionUrl;
            setStoredMood(currentDate, selectedEmotion);
            updateMoodImage(currentDate, selectedEmotion, selectedImagesContainer);
            modal.remove();
            updateCalendar();
        });

        selectedImagesContainer.appendChild(emotionImage);
    });

    modal.appendChild(selectedImagesContainer);
    document.body.appendChild(modal);
}

function updateMoodImage(currentDate, emotionUrl, selectedImagesContainer) {
    const dayCell = document.querySelector(`[data-date="${currentDate.toISOString().split('T')[0]}"]`);
    const moodSection = dayCell.querySelector('.mood-section');

    // Supprimez le contenu existant de la section d'humeur
    moodSection.innerHTML = '';

    // Ajoutez l'image sélectionnée à la section d'humeur
    const selectedImage = document.createElement('img');
    selectedImage.src = emotionUrl;
    selectedImage.alt = 'Émotion sélectionnée';
    selectedImage.className = 'selected-emotion-image';

    moodSection.appendChild(selectedImage);

    // Ajoutez l'image sélectionnée à la section des images sélectionnées
    const selectedImageCopy = document.createElement('img');
    selectedImageCopy.src = emotionUrl;
    selectedImageCopy.alt = 'Émotion sélectionnée';
    selectedImageCopy.className = 'selected-emotion-image';

    selectedImagesContainer.appendChild(selectedImageCopy);
}

document.addEventListener('DOMContentLoaded', () => {
    setInitialWeek();
    updateCalendar();
});

function updateCalendar() {
    const weekHeader = document.getElementById('week');
    const calendarBody = document.getElementById('calendar-body');

    // Effacer le contenu du corps du calendrier
    calendarBody.innerHTML = '';

    // Mettre à jour l'en-tête avec la semaine actuelle
    const currentWeekEnd = new Date(currentWeekStart);
    currentWeekEnd.setDate(currentWeekEnd.getDate() + 6);
    weekHeader.textContent = `Semaine ${currentWeekStart.toLocaleDateString()} - ${currentWeekEnd.toLocaleDateString()}`;

    // Créer les cellules pour chaque jour de la semaine
    for (let i = 0; i < 7; i++) {
        const dayCell = document.createElement('td');
        const currentDate = new Date(currentWeekStart);
        currentDate.setDate(currentWeekStart.getDate() + i);

        dayCell.textContent = currentDate.getDate();
        dayCell.setAttribute('data-date', currentDate.toISOString().split('T')[0]);

        // Ajouter la section d'humeur (image et cause)
        const moodSection = document.createElement('div');
        moodSection.className = 'mood-section';

        const moodButton = document.createElement('button');
        moodButton.textContent = 'Choisir une humeur';
        moodButton.addEventListener('click', () => {
            showEmotionSelector(currentDate);
        });

        // Ajouter la section pour afficher l'image sélectionnée
        const selectedImagesContainer = document.createElement('div');
        selectedImagesContainer.className = 'selected-images-container';

        // Ajouter un espace pour les images sélectionnées
        const selectedImage = document.createElement('img');
        selectedImage.className = 'selected-emotion-image';
        selectedImagesContainer.appendChild(selectedImage);

        // Ajouter la section de cause
        const causeInput = document.createElement('input');
        causeInput.type = 'text';
        causeInput.className = 'cause';
        causeInput.placeholder = 'Écrire la cause';

        causeInput.addEventListener('input', () => {
            setStoredCause(currentDate, causeInput.value);
        });

        const storedCause = getStoredCause(currentDate);
        if (storedCause) {
            causeInput.value = storedCause;
        }

        moodSection.appendChild(moodButton);
        moodSection.appendChild(selectedImagesContainer); // Ajouter l'espace pour les images sélectionnées
        moodSection.appendChild(causeInput);

        dayCell.appendChild(moodSection);
        calendarBody.appendChild(dayCell);
    }

    // Augmenter la hauteur du calendrier
    const calendar = document.querySelector('.calendar');
    calendar.style.minHeight = '600px'; // Vous pouvez ajuster la hauteur selon vos besoins
}

function setStoredMood(date, mood) {
    localStorage.setItem(getStorageKey(date, 'mood'), mood);
}

function getStoredCause(date) {
    return localStorage.getItem(getStorageKey(date, 'cause'));
}

function setStoredCause(date, cause) {
    localStorage.setItem(getStorageKey(date, 'cause'), cause);
}

function getStorageKey(date, section) {
    return `${date.toISOString().split('T')[0]}-${section}`;
}

function previous() {
    currentWeekStart.setDate(currentWeekStart.getDate() - 7);
    updateCalendar();
}

function next() {
    currentWeekStart.setDate(currentWeekStart.getDate() + 7);
    updateCalendar();
}

