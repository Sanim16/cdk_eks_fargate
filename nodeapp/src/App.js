import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
        This is a CICD project that dockerises a nodejs website created with "npx create-react-app".

        The code is pushed to GitHub, where a GitHub Actions workflow uses AWS CDK to provision the Infrastructure on AWS.

        The docker image is pushed to AWS ECR from where it is run on the provisioned EKS Fargate cluster.

        The deployment is managed by GitHub Actions
        </p>
        <a
          className="App-link"
          href="https://github.com/Sanim16/cdk_eks_fargate"
          target="_blank"
          rel="noopener noreferrer"
        >
          Link to the GitHub Repo
        </a>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
