const C = 'baobab-reader-v25';
const CORE = [
  './',
  'index.html',
  'style.css',
  'app.js',
  'stories-data.js',
  'front-matter.js',
  'quiz-data.js',
  'stories.json',
  'assets/fonts/Ubuntu-R.ttf',
  'assets/fonts/Ubuntu-M.ttf',
  'assets/fonts/Ubuntu-B.ttf',
  'assets/fonts/Ubuntu-RI.ttf'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(C).then(cache => cache.addAll(CORE)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(key => key !== C).map(key => caches.delete(key))
    )).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);

  // Network-first for code, markup, data and image assets so updates reflect immediately
  const isNetworkFirst = /\.(?:html|css|js|json|svg|png|jpg|jpeg|webp)$/.test(url.pathname) || url.pathname.endsWith('/');

  if (isNetworkFirst) {
    event.respondWith(
      fetch(event.request)
        .then(response => {
          if (response && response.status === 200) {
            const copy = response.clone();
            caches.open(C).then(cache => cache.put(event.request, copy));
          }
          return response;
        })
        .catch(() => caches.match(event.request))
    );
  } else {
    event.respondWith(
      caches.match(event.request).then(hit => hit || fetch(event.request).then(response => {
        if (response && response.status === 200) {
          const copy = response.clone();
          caches.open(C).then(cache => cache.put(event.request, copy));
        }
        return response;
      }))
    );
  }
});