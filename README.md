# Candle Whisperer API

This is a modern React + TypeScript starter project using Vite, Tailwind CSS, and shadcn-ui components. It provides a clean foundation for building your own web application, with a focus on rapid development and customization.

## Features
- ⚡️ Fast development with Vite
- 🎨 Utility-first styling with Tailwind CSS
- 🧩 Accessible, customizable UI components (shadcn-ui)
- 🛣️ Client-side routing (react-router-dom)
- 🧹 Pre-configured for best practices

## Getting Started

### 1. Install dependencies
```sh
npm install
```

### 2. Start the development server
```sh
npm run dev
```

Visit [http://localhost:8080](http://localhost:8080) to view your app.

### 3. Build for production
```sh
npm run build
```

### 4. Preview the production build
```sh
npm run preview
```

## Project Structure
- `src/` — Main source code
  - `components/ui/` — Ready-to-use UI components
  - `pages/` — App pages (add your own here)
  - `hooks/`, `lib/` — Utilities and custom hooks
- `public/` — Static assets
- `index.html` — HTML entry point

## Customization
- Add your own pages in `src/pages/` and update routes in `src/App.tsx`.
- Use and customize UI components from `src/components/ui/`.
- Update styles and design tokens in `src/index.css` and `tailwind.config.ts`.

## Database
This template does **not** include any database integration. You are free to set up your own backend or database solution as needed.

## Backend API (Python + FastAPI)

A Python FastAPI backend is included in the `backend/` directory. This serves as the API for your application.

### How to run the backend

1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Follow the instructions in `backend/README.md` to set up and run the API server.

See [`backend/README.md`](backend/README.md) for more details.

## License
MIT
