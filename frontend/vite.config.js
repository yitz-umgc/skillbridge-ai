import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/employees": "http://localhost:8000",
      "/projects": "http://localhost:8000",
      "/match": "http://localhost:8000",
    },
  },
});
