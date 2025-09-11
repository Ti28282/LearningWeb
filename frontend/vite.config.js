import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    // Дополнительные опции (по желанию):
    port: 3000, // можно указать конкретный порт
    open: true  // автоматически открывать браузер
  }
})
