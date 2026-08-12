import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Flask + EdgeOne Pages | EdgeOne Makers",
  description: "Deploy Flask web applications as serverless functions on EdgeOne Pages. The most popular Python micro web framework, now serverless. · Demo only · EdgeOne Makers",
  keywords: "EdgeOne Makers, Demo only",
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
