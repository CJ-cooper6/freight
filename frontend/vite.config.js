import { defineConfig } from "vite";
import vue from '@vitejs/plugin-vue';
 
export default defineConfig({
  plugins: [vue()],
  server: {
    host: "0.0.0.0",
    port: '5173',
    https: false,
    proxy: {
      "/api": {
        target: "http://localhost:5000",
        changeOrigin: true,
        ws: true,
      }
    },
  },
});