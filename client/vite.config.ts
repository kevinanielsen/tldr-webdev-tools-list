import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  server: {
    proxy: {
      '/api': 'http://localhost:8000',
    }
  },
  plugins: [svelte(), VitePWA({
    registerType: 'autoUpdate',
    includeAssets: ['apple-touch-icon-180x180.png', 'maskable-icon-512x512.png, favicon.ico'],
    manifest: {
      name: 'TLDR Web Dev Tools',
      short_name: 'TLDR Web Dev Tools',
      description: 'A list of the web dev tools featured in TLDR Web Dev news letter.',
      theme_color: '#ffffff',
      background_color: '#ffffff',
      display: 'standalone',
      icons: [
        {
          src: 'pwa-64x64.png',
          sizes: '64x64',
          type: 'image/png'
        },
        {
          src: 'pwa-192x192.png',
          sizes: '192x192',
          type: 'image/png'
        },
        {
          src: 'pwa-512x512.png',
          sizes: '512x512',
          type: 'image/png'
        }
      ]
    }
  })],
  base: "./", // This will make paths relative
  build: {
    emptyOutDir: true,
    outDir: 'dist', // Where we want to put the build
    assetsDir: 'assets', // This will be folder inside the public
    rollupOptions: {
      input: {
        main: './index.html', // This index.html will be in public folder
      },
      output: {
        entryFileNames: 'assets/js/[name]-[hash].js', // Here we put all js files into js folder
        chunkFileNames: 'assets/js/[name]-[hash].js',
        assetFileNames: ({ name }) => {
          if (/\.(gif|jpe?g|png|svg)$/.test(name ?? '')) {
            return 'assets/images/[name].[ext]';
          }

          if (/\.css$/.test(name ?? '')) {
            return 'assets/css/[name]-[hash].[ext]';
          }

          return 'assets/[name]-[hash].[ext]';
        },
      }
    }
  }
})
