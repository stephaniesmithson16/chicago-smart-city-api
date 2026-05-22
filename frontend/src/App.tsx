import { useEffect, useState } from "react";

import "./App.css";

const PAGE_SIZE = 25;

function formatRisk(risk: string) {
  return risk.match(/\(([^)]+)\)/)?.[1] ?? risk;
}

type Inspection = {
  inspection_id: number;
  name: string;
  aka_name: string;
  license: string;
  facility_type: string;
  address: string;
  zip_code: string;
  risk: string;
  results: string;
  inspection_date: string;
  inspection_type: string;
  violations: string;
};

function App() {
  const [inspections, setInspections] = useState<Inspection[]>([]);
  const [loading, setLoading] = useState(true);
  const [offset, setOffset] = useState<number>(0);
  const [zipCode, setZipCode] = useState("");
  const [result, setResult] = useState("");
  const [risk, setRisk] = useState("");

  useEffect(() => {
    async function fetchInspections() {
      try {
        setLoading(true);
        const params = new URLSearchParams();

        params.set("limit", "25");
        params.set("offset", offset.toString());

        if (zipCode) params.set("zip_code", zipCode);
        if (result) params.set("result", result);
        if (risk) params.set("risk", risk);

        const response = await fetch(
          `http://127.0.0.1:8000/api/v1/restaurants/inspections?${params.toString()}`
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
  }, [offset, zipCode, result, risk]);

  return (
    <main
      style={{ padding: "2rem", fontFamily: "sans-serif", fontSize: "16px" }}
    >
      <h1>Chicago Restaurant Inspections</h1>

      <input
        value={zipCode}
        onChange={(event) => setZipCode(event.target.value)}
        placeholder="Zip code"
      />

      <select value={result} onChange={(event) => setResult(event.target.value)}>
        <option value="">All results</option>
        <option value="Pass">Pass</option>
        <option value="Fail">Fail</option>
        <option value="Pass w/ Conditions">Pass w/ Conditions</option>
      </select>

      <select value={risk} onChange={(event) => setRisk(event.target.value)}>
        <option value="">All risks</option>
        <option value="Risk 1 (High)">High</option>
        <option value="Risk 2 (Medium)">Medium</option>
        <option value="Risk 3 (Low)">Low</option>
      </select>

      {loading ? (
        <p>Loading inspections...</p>
      ) : (
        <div className="table-container">
        <table
          style={{
            borderCollapse: "separate",
            borderColor: "#ddd",
            width: "100%",
            marginTop: "2rem",
          }}
        >
          <colgroup>
            <col className="name-column" />
            <col />
            <col />
            <col />
            <col />
            <col />
            <col />
            <col />
            <col className="date-column" />
            <col className="violations-column" />
          </colgroup>
          <thead>
            <tr>
              <th className="name-cell">Name</th>
              <th>Facility</th>
              <th>Address</th>
              <th>Zip</th>
              <th>Risk</th>
              <th>Result</th>
              <th>Type</th>
              <th className="date-cell">Date</th>
              <th>Violations</th>
            </tr>

          </thead>

          <tbody>
            {inspections.map((inspection) => (
              <tr key={inspection.inspection_id}>
                <td className="name-cell">{inspection.name}</td>
                <td>{inspection.facility_type}</td>
                <td>{inspection.address}</td>
                <td>{inspection.zip_code}</td>
                <td>{formatRisk(inspection.risk)}</td>
                <td>{inspection.results}</td>
                <td>{inspection.inspection_type}</td>
                <td className="date-cell">{inspection.inspection_date}</td>
                <td className="violations-cell">
                  <div className="violations-preview">
                    {inspection.violations || "No violations"}
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        </div>
      )}
      <div style={{ display: "flex",
        alignItems: "center",
        justifyContent: "center",
        marginTop: "2rem",
        gap: "2rem"}}>
        <button
          style={{
            padding: "0.5rem 1rem",
            fontSize: "16px",
            cursor: "pointer",
          }}
          onClick={() => {
            setOffset((currentOffset) => Math.max(currentOffset - PAGE_SIZE, 0));
          }}
          disabled={offset === 0}
        >
          Back
        </button>
        <button
          style={{
            padding: "0.5rem 1rem",
            fontSize: "16px",
            cursor: "pointer",
          }}
          onClick={() => {
            setOffset((currentOffset) => currentOffset + PAGE_SIZE);
          }}
        >
          Next
        </button>
      </div>
    </main>
  );
}

export default App;
