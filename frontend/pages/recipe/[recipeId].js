import Head from "next/head";
import { useRouter } from "next/router";

export default function Home() {
  const router = useRouter();
  const { recipeId } = router.query;
  return (
    <div>
      <Head>
        <title>Pantry Pirate | Create</title>
      </Head>
      <div className="container">
        <div className="columns is-centered">
          <div className="box column is-6">
            <h1 className="title">This is recipe {recipeId}</h1>
          </div>
        </div>
      </div>
    </div>
  );
}
