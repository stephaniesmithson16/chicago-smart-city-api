import { useEffect, useState } from "react";

type Inspection = {
  inspection_id: string;
  name: string;
  address: string;
  zip_code: string;
  risk: string;
  results: string;
  inspection_date: string;
};

function App() {
  const [inspections, setInspections] = useState<Inspection[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchInspections() {
      try {
        const response = await fetch(
          "http://127.0.0.1:8000/api/v1/restaurants/inspections?limit=25"
        );

        const data = await response.json();

        setInspections(data);
      } catch (error) {
        console.error("Failed to fetch inspections:", error);
      } finally {
        setLoading(false);
      }
    }

    fetchInspections();
  }, []);

  return (
    <main style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>Chicago Smart City Dashboard</h1>

      {loading ? (
        <p>Loading inspections...</p>
      ) : (
        <table
          style={{
            borderCollapse: "collapse",
            width: "100%",
            marginTop: "2rem",
          }}
        >
          <thead>
            <tr>
              <th>Name</th>
              <th>Address</th>
              <th>Zip</th>
              <th>Risk</th>
              <th>Result</th>
              <th>Date</th>
            </tr>
          </thead>

          <tbody>
            {inspections.map((inspection) => (
              <tr key={inspection.inspection_id}>
                <td>{inspection.name}</td>
                <td>{inspection.address}</td>
                <td>{inspection.zip_code}</td>
                <td>{inspection.risk}</td>
                <td>{inspection.results}</td>
                <td>{inspection.inspection_date}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </main>
  );
}

export default App;
