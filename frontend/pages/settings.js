import Head from "next/head";
import Details from "../components/settings/Details"
import Password from "../components/settings/Password"

export default function Home() {
  return (
    <div>
      <Head>
        <title>Pantry Pirate | Settings</title>
      </Head>
      <div className="container">
        <div className="columns is-centered">
          <div className="box column is-10">
            <h1 className="title is-1">Settings</h1>
            <Details/>
            <Password/>
          </div>
        </div>
      </div>
    </div>
  );
}
