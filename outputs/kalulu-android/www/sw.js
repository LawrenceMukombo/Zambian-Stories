const C='baobab-reader-v18';
const CORE=['./','index.html','style.css','app.js','stories-data.js','front-matter.js','quiz-data.js','stories.json','assets/fonts/Ubuntu-R.ttf','assets/fonts/Ubuntu-M.ttf','assets/fonts/Ubuntu-B.ttf','assets/fonts/Ubuntu-RI.ttf','assets/covers/story-01.jpg','assets/covers/story-02.jpg','assets/covers/story-03.jpg','assets/covers/story-04.jpg','assets/covers/story-05.jpg','assets/covers/story-06.jpg','assets/covers/story-07.jpg','assets/covers/story-08.jpg','assets/covers/story-09.jpg','assets/covers/story-10.jpg','assets/covers/story-11.jpg','assets/covers/story-12.jpg','assets/covers/story-13.jpg','assets/covers/story-14.jpg','assets/covers/story-15.jpg','assets/covers/story-16.jpg','assets/covers/story-17.jpg','assets/covers/story-18.jpg','assets/covers/story-19.jpg','assets/covers/story-20.jpg','assets/covers/story-21.jpg','assets/covers/story-22.jpg','assets/covers/story-23.jpg','assets/covers/story-24.jpg','assets/covers/story-25.jpg'];
self.addEventListener('install',event=>event.waitUntil(caches.open(C).then(cache=>cache.addAll(CORE)).then(()=>self.skipWaiting())));
self.addEventListener('activate',event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(key=>key!==C).map(key=>caches.delete(key)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',event=>{
  if(event.request.method!=='GET')return;
  const url=new URL(event.request.url);
  const fresh=/\.(?:html|css|js|json)$/.test(url.pathname)||url.pathname.endsWith('/');
  if(fresh){
    event.respondWith(fetch(event.request).then(response=>{const copy=response.clone();caches.open(C).then(cache=>cache.put(event.request,copy));return response}).catch(()=>caches.match(event.request)));
  }else{
    event.respondWith(caches.match(event.request).then(hit=>hit||fetch(event.request).then(response=>{const copy=response.clone();caches.open(C).then(cache=>cache.put(event.request,copy));return response})));
  }
});