const SERVER_PATH = 'http://localhost:8080';

/**
 * Fetches json data from a specified url.
 * 
 * @async
 * @param url {string} The url to fetch from
 * @param params {RequestInit} [params={}] Optional request parameters.
 * @returns {Promise<Object | null>} A Promise that resolves to the fetched JSON
 * @throws {Error} If the response is not ok or the JSON contains an error
 */
const json_fetch = async (url, params = {}) => {
    try {
        params = { ...params, credentials: 'include', headers: { 'Content-Type': 'application/json' } };
        const response = await fetch(url, params);

        if (response.status === 204)
            return null;

        const data = await response.json();
        if (response.ok)
            return data;

        console.error(data);
    } catch(e) {
        console.error(e);
    }
};

let me = null;

// ==================================================
// auth form management
// ==================================================
(() => {
    const el_auth_form = document.getElementById('container-auth_form');
    if (!el_auth_form)
        return;

    const messages = {
        'register': 'Vous avez déjà un compte ?',
        'login': 'Vous n\'avez pas encore de compte ?',
    };

    const el_title = el_auth_form.querySelector('.form-title');


    const form = el_auth_form.querySelector('form');
    let action = form.action;
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = {};
        (new FormData(form)).forEach((value, key) => data[key] = value);
        
        const response = await json_fetch(action, { method: 'POST', body: JSON.stringify(data) });
        if (!response)
            return;

        me = response.data;
        location.reload();
    });

    const el_switch_container = el_auth_form.querySelector('.form-switch-container');
    const el_switch = el_auth_form.querySelector('.form-switch');

    el_switch.addEventListener('click', () => {
        action = action.includes('/login') ? '/register' : '/login';
        el_title.textContent = action === '/login' ? 'Connexion' : 'Inscription';
        el_switch_container.childNodes[1].textContent = messages[action.slice(1)];
        el_switch.textContent = action === '/login' ? 'Inscription' : 'Connexion';
    });
})();

// ==================================================
// emotion form management
// ==================================================
(() => {
    const el_emotion_form = document.getElementById('container-emotion_form');
    if (!el_emotion_form)
        return;

    el_emotion_form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = {};
        (new FormData(el_emotion_form)).forEach((value, key) => data[key] = value);

        const response = await json_fetch('/emotion', { method: 'POST', body: JSON.stringify(data) });
        if (!response)
            return;

        location.replace('/emotions');
        location.reload();
    });
})();