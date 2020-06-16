import Head from "next/head";

import Hello from "../components/Hello";

export default function Home() {
  return (
    <div className="container">
      <div className="columns is-centered">
        <div className="box column is-6">
          <h1 className="title">Welcome to PantryPirate</h1>
          <p>Probs good idea to read README.md</p>
          <Hello />
        </div>
      </div>
    </div>
  );
}
