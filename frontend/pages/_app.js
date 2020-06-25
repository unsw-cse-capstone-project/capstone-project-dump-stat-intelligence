import "../styles/styles.scss";

import Head from "next/head";
import Nav from "../components/nav/Nav";

export default function PantryPirate({ Component, pageProps }) {
  return (
    <div>
      <Head>
        <title>Pantry Pirate</title>
        <meta charSet="utf-8" />
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>
      <Nav />
      <Component {...pageProps} />
    </div>
  );
}
