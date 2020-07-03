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

  handleSubmit = async (e) => {
    RecipeAPI.create(this.state.recipe, "").then((res) => {
      console.log(res);
    });
  };

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
                  <input
                    className="input"
                    placeholder="Title"
                    value={this.state.recipe.title}
                    onChange={(e) =>
                      this.setState((prev) => ({
                        recipe: { ...prev, title: e.target.value },
                      }))
                    }
                  />
                </div>
                <div className="field">
                  <label className="label">Author ID (for the demo)</label>
                  <input
                    className="input"
                    placeholder="Author Id"
                    value={this.state.recipe.author}
                    onChange={(e) =>
                      this.setState((prev) => ({
                        recipe: { ...prev, author: e.target.value },
                      }))
                    }
                  />
                </div>
                <div className="field">
                  <label className="label">Cook Time</label>
                  <input
                    className="input"
                    placeholder="Cook Time"
                    value={this.state.recipe.cook_time}
                    onChange={(e) =>
                      this.setState((prev) => ({
                        recipe: { ...prev, cook_time: e.target.value },
                      }))
                    }
                  />
                </div>
                <div className="field">
                  <label className="label">Method</label>
                  <textarea
                    className="textarea"
                    placeholder="Method"
                    value={this.state.recipe.method}
                    onChange={(e) =>
                      this.setState((prev) => ({
                        recipe: { ...prev, method: e.target.value },
                      }))
                    }
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
