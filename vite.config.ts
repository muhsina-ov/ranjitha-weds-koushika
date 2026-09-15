import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tsconfigPaths from "vite-tsconfig-paths";
import tailwindcss from "@tailwindcss/vite";

// True SPA build — no TanStack Start, no Nitro, no SSR.
export default defineConfig({
  base: "./",
  plugins: [react(), tsconfigPaths(), tailwindcss()],
});
