import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

export default defineConfig({
  server: {
    proxy: {
      '/api': 'http://localhost:8000',
    }
  },
  plugins: [svelte()],
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
