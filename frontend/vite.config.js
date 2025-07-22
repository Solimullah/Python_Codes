import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  preview: {
    port: Number(process.env.PORT) || 4173,
    host: true,
  plugins: [react()],
})
