import "../styles/styles.scss";

import Head from "next/head";
import Nav from "../components/nav/Nav";
import PantryButton from "../components/Pantry/PantryButton";

export default function PantryPirate({ Component, pageProps }) {
  return (
    <>
      <Head>
        <title>Pantry Pirate</title>
        <meta charSet="utf-8" />
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>
      <Nav />
      <main>
        <div className="container">
          <Component {...pageProps} />
        </div>
        <PantryButton />
      </main>
    </>
  );
}
