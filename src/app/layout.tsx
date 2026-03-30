import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Flask + EdgeOne Pages",
  description: "Deploy Flask web applications as serverless functions on EdgeOne Pages. The most popular Python micro web framework, now serverless.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en-US">
      <head>
        <link rel="icon" href="/flask-favicon.svg" />
      </head>
      <body
        className="antialiased"
      >
        {children}
      </body>
    </html>
  );
}
