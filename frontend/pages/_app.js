import "../styles/styles.scss";
import Nav from "../components/nav/Nav";

export default function PantryPirate({ Component, pageProps }) {
  return (
    <div>
      <Nav />
      <Component {...pageProps} />
    </div>
  );
}
