import Head from "next/head";
import { withRouter } from "next/router";
import React from "react";

import RecipeAPI from "../../lib/api/recipe";
import Error from "../../components/Error/Error";

class Recipe extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: false,
      recipe: {
        title: "",
        method: "",
        cook_time: "",
        author: "",
      },
      error: null,
    };
  }

  componentDidMount() {}

  handleDelete = async (e) => {};

  render() {
    if (this.state.error) {
      return <Error message={this.state.error.statusText} />;
    }

    if (this.state.loading) {
      return <p>Loading</p>;
    }
    return (
      <>
        <Head>
          <title>Pantry Pirate | Create</title>
        </Head>
        <div className="container">
          <div className="columns is-centered">
            <div className="box column is-10">
              <h1 className="title">New Recipe</h1>
              <form>
                <div className="field">
                  <label className="label">Title</label>
                  <input className="input" placeholder="Title" />
                </div>
                <div className="field">
                  <label className="label">Cook Time</label>
                  <input className="input" placeholder="Cook Time" />
                </div>
                <div className="field">
                  <label className="label">Method</label>
                  <textarea
                    className="textarea"
                    placeholder="Method"
                  ></textarea>
                </div>
              </form>
              <br />

              <div className="buttons">
                <button className="button is-light is-success">
                  Add Recipe
                </button>
                <button className="button is-light is-danger">Discard</button>
              </div>
            </div>
          </div>
        </div>
      </>
    );
  }
}

// You can't use hooks (i.e. useRouter) with a class component in react
export default withRouter(Recipe);
